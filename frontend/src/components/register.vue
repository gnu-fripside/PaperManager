<template>
  <div class="register" style="width:300px;margin-left:auto;margin-right:auto;">
    <el-form ref="form" :model="form" :rules="rules">
   <el-form-item label="email"  prop="email">
      <el-input type="text" placeholder="input email" v-model="form.email" size="large"></el-input>
    </el-form-item>    
    <el-form-item label="username" prop="username">
      <el-input type="text" placeholder="input user id" v-model="form.username" size="large"></el-input>
    </el-form-item>
    <el-form-item label="password" prop="password">
      <el-input type="password" placeholder="input password" v-model="form.password" size="large"></el-input>
    </el-form-item>
     <el-form-item class="enter"  style="margin: 20px 0">
      <el-button type="success" @click="register">register</el-button>
      <el-button type="success" @click="gotologin">Go to login</el-button>
    </el-form-item>
    </el-form>
    <br>
    <div>{{ status }}</div>
  </div>
</template>

<script>
  export default {
    name: 'register',
    data () {
      return {
        form : {
            username: "",
            password: "",
            email: ""
            },
        status: "",
        rules: {
            email:[
                { required: true, message: 'please input email address', trigger: 'blur' },
                { type: 'email', message: 'invalid email address', trigger: 'blur,change' }
                ] ,
            username: [
                { required: true, message: 'please input user name', trigger: 'blur' }
                ] ,
            password: [
                { required: true, message: 'please input password', trigger: 'blur' }
                ]
        }
      }
    },
    
    methods: {
      register: function () {
        var axios = require('axios')
        var qs = require('qs')
        axios.post('/api/register',
                    qs.stringify({ username: this.form.username,
                      password: this.form.password,
                      email: this.form.email })
                    )
          .then((response) => {
            var res = response.data
            if (res['error_num'] == 0) {
              this.status = 'succeed'
              this.$router.push({path:'/login'})
            } else {
              this.status = res['msg']
            }
          })
      },
      gotologin: function () {
        this.$router.push({path:'/login'})
      },
    },
  }
</script>
