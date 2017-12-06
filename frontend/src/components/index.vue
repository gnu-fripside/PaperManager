<template>
  <div class="index">
    <h1>Paper Manager</h1>
    <p>
      <router-link to="/login">
        <el-button>login</el-button>
      </router-link>
      <router-link to="/register">
        <el-button>register</el-button>
      </router-link>
      <router-link to="/showPdf">
        <el-button>show pdf</el-button>
      </router-link>
      <router-link to="/tag">
        <el-button>tag tree</el-button>
      </router-link>
    </p>
  </div>
</template>

<script>
  // import vue-router from 'vue-router'

  export default {
    name: 'index',
  }
</script>
