<template>
  <div class="index">
    <!--
    <header class="header">
      <el-row>
        <el-col :span="24">
          <el-menu default-active="5" class="el-menu-demo" mode="horizontal" @select="">
            <el-menu-item index="1">Paper</el-menu-item>
            <el-menu-item index="2">Tag Tree</el-menu-item>
            <el-menu-item index="3">Import/Export</el-menu-item>
            <el-menu-item index="4">Profile</el-menu-item>
            <el-menu-item index="5">Help</el-menu-item>
          </el-menu>
        </el-col>
      </el-row>
    </header>
    -->
    <div style="position: relative;height: 10px;width: 100%;"></div>

    <main>
      <!-- 左侧导航 -->
      <div class="main-left">
        <el-menu default-active="showPdf" class="el-menu-vertical-demo" :router="true">
          <!-- el-menu-item index="showPdf" :route="{name:'showPdf'}" :class="{'isActive': active}">Paper</el-menu-item -->
          <el-menu-item index="tagTree" :route="{name:'tagTree'}" :class="{'isActive': !active}">Go back!</el-menu-item>
          <!-- el-menu-item index="fileInfo" :route="{name:'fileInfo'}" :class="{'isActive': !active}">File Info</el-menu-item -->
        </el-menu>
      </div>

      <!-- 右侧主内容区 -->
      <div  class="main-right">
        <router-view></router-view>
      </div>
    </main>

  </div>
</template>

<script>
  // import vue-router from 'vue-router'

  export default {
  name: 'index',
  }
</script>

<style>
  body{margin: 0;}
  #app {
  min-width: 1200px;
  margin: 0 auto;
  font-family: "Helvetica Neue","PingFang SC",Arial,sans-serif;
  }
  /* 头部导航 */
  header{z-index: 1000;min-width: 1200px;transition: all 0.5s ease;  border-top: solid 4px #3091F2;  background-color: #fff;  box-shadow: 0 2px 4px 0 rgba(0,0,0,.12),0 0 6px 0 rgba(0,0,0,.04);  }
  header.header-fixed{position: fixed;top: 0;left: 0;right: 0;}
  header .el-menu-demo{padding-left: 300px!important;}

  /* 主内容区 */
  main{    display: -webkit-box;  display: -ms-flexbox;  display: flex;  min-height: 800px; min-width: 1300px;  border: solid 10px #E9ECF1;  background-color: #FCFCFC;  }
  main .main-left{text-align: center;width: 100px;float: left;}
  main .main-right{-webkit-box-flex: 1;  -ms-flex: 1;  flex: 1;  background-color: #fff; padding: 10px 10px; }
  main .el-menu{background-color: transparent!important;}
</style>

