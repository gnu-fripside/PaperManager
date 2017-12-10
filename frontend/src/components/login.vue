<template>
  <div class="login" style="width:300px;margin-left:auto;margin-right:auto;">
    <div>
      <el-input type="text" placeholder="input user id" v-model="userId" size="large">user</el-input>
    </div>
    </br>
    <div>
      <el-input type="password" placeholder="input password" v-model="password" size="large">password</el-input>
    </div>
    <div>{{ status }}</div>
    <div style="margin: 20px 0" >
      <el-button type="success" @click="login">login</el-button>
      <el-button type="success" @click="register">register</el-button>
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
<script>
  export default {
    name: 'register',
    data () {
      return {}
    },
    methods: {
      register: function () {
        this.$router.push({path:'/register'})
      },
    },
  }
</script>
