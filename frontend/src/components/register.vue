<template>
  <div class="register">
    <div>
      <input type="text" placeholder="input user id" v-model="userId"></input>
      <input type="password" placeholder="input password" v-model="password"></input>
    </div>
    <div>{{ status }}</div>
    <div class="enter">
      <button type="success" @click="register">register</button>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'register',
    data () {
      return {
        userId: "",
        password: "",
        status: ""
      }
    },
    methods: {
      register: function () {
        this.$http.get('http://127.0.0.1:8080/api/register?userId=' + this.userId + '&password=' + this.password)
          .then((response) => {
            var res = JSON.parse(response.bodyText)
            if (res['error_num'] == 0) {
              this.status = 'succeed'
              // go back
            } else {
              this.status = res['msg']
            }
          })
      },
    },
  }
</script>
