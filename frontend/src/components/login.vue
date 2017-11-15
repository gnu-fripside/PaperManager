<template>
  <div class="login">
    <div>
      <input type="text" placeholder="input user id" v-model="userId"></input>
      <input type="password" placeholder="input password" v-model="password"></input>
    </div>
    <div>{{ status }}</div>
    <div>
      <button type="success" @click="login">login</button>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'login',
    data () {
      return {
        userId: "",
        password: "",
        status: ""
      }
    },
    methods: {
      login: function () {
        this.$http.get('http://127.0.0.1:8080/api/login?userId=' + this.userId + '&password=' + this.password)
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
