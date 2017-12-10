import Element from 'element-ui'
import 'element-ui/lib/theme-default/index.css'
Vue.use(Element)

<template>
<el-container>
  <el-header height="95px" style="background:#3091f2;">
  <div id="app">
    <img src="./assets/logo-90px.png">
  </div>
  </el-header>
  <el-main>
    <router-view/> 
  </el-main>
</el-container>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #3091f2;
}
</style>
