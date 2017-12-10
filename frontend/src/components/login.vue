<template>
  <div class="login" style="width:300px;margin-left:auto;margin-right:auto;">
    <el-form ref="form" :model="form" >
    <el-form-item label="username">
      <el-input type="text" placeholder="input user id" v-model="username" size="large">user</el-input>
    </el-form-item>
    <el-form-item label="password">
      <el-input type="password" placeholder="input password" v-model="password" size="large">password</el-input>
    </el-form-item> 
    <el-form-item style="margin: 20px 0" >
      <el-button type="success" @click="login">login</el-button>
      <el-button type="success" @click="register">register</el-button>
    </el-form-item>
    </el-form>
    <br>
    <div>{{ status }}</div>
  </div>
</template>

<script>
  export default {
    name: 'login',
    data () {
      return {
        form:{
          username: "",
          password: "",
          status: ""
        }
      }
    },
    methods: {
      login: function () {
        this.$http.post('http://127.0.0.1:8080/api/login',{param:{username:this.usernamea,password:this.password}})
          .then((response) => {
            var res = JSON.parse(response.bodyText)
            if (res['error_num'] == 0) {
              this.status = 'succeed'
              let expireDays = 1000 * 60 * 60 * 24 * 30;
              this.setCookie('session', response.data.session, expireDays);
              this.$router.push({path:'/'})
              // go back
            } else {
              this.status = res['msg']
            }
          })
      },
      register: function () {
        this.$router.push({path:'/register'})
      },
    },
  }
</script>