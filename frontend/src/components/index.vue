<template>
  <div class="index">
    <h1>Paper Manager</h1>
    <p>
      <router-link to="/login">login</router-link>
      <router-link to="/register">register</router-link>
      <router-link to="/showPdf">show pdf</router-link>
      <router-link to="/tag">tag tree</router-link>
    </p>
  </div>
</template>

<script>
  // import vue-router from 'vue-router'

  export default {
    name: 'index',
  }
</script>
