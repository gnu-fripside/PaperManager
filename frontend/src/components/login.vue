<template>
  <div class="login" style="width:300px;margin-left:auto;margin-right:auto;">
    <el-form ref="form" :model="form" >
    <el-form-item label="username">
      <el-input type="text" placeholder="input user id" v-model="form.username" size="large">user</el-input>
    </el-form-item>
    <el-form-item label="password">
      <el-input type="password" placeholder="input password" v-model="form.password" size="large">password</el-input>
    </el-form-item> 
    <el-form-item style="margin: 20px 0" >
      <el-button type="primary" @click="login">login</el-button>
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
        },
          status: ""
      }
    },
    methods: {
    /*
      login: function () {
        var axios = require('axios')
        var qs = require('qs')
         axios.post('/api/login',
                    qs.stringify({ username: this.form.username,
                      password: this.form.password })
                    )
          .then((response) => {

            var res = response.data

            if (res['error_num'] == 0) {
              this.status = 'succeed'
              let expireDays = 1000 * 60 * 60 * 24 * 30;
              // this.setCookie('username', this.form.username, expireDays);
              // this.setCookie('session', response.data.session, expireDays);
              this.$router.push({name: 'index', params: {name: this.form.username}});
            } else {
              this.status = res['msg']
              alert(res['msg'])
            }
          })
      },
    */
        login: function () {
            this.status = 'succeed'
            let expireDays = 1000 * 60 * 60 * 24 * 30;
            this.$router.push({name: 'index', params: {name: this.form.username}});
        }, 
      register: function () {
        this.$router.push({path:'/register'})
      },
    },
  }
</script>
