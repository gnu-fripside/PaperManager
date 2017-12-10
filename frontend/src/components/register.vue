<template>
  <div class="register" style="width:300px;margin-left:auto;margin-right:auto;">
    <el-form ref="form" :model="form" >
    <el-form-item label="username">
      <el-input type="text" placeholder="input user id" v-model="username" size="large"></el-input>
    </el-form-item>
    <el-form-item label="password">
      <el-input type="password" placeholder="input password" v-model="password" size="large"></el-input>
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
        userId: "",
        password: "",
        status: ""
      }
    },
    methods: {
      register: function () {
        this.$http.get('http://127.0.0.1:8080/api/register',{param:{username:this.username,password:this.password}})
          .then((response) => {
            var res = JSON.parse(response.bodyText)
            if (res['error_num'] == 0) {
              this.status = 'succeed'
              this.$router.push({path:'/login'})
              // go back
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
