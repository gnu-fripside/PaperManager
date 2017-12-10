<template>
  <div class="register" style="width:300px;margin-left:auto;margin-right:auto;">
    <div>
      <el-input type="text" placeholder="input user id" v-model="userId" size="large"></el-input>
    </div>
    <br>
    <div>
      <el-input type="password" placeholder="input password" v-model="password" size="large"></el-input>
    </div>
    <div>{{ status }}</div>
    <div class="enter"  style="margin: 20px 0">
      <el-button type="success" @click="register">register</el-button>
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
