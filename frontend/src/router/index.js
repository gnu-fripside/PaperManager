import Vue from 'vue'
import Router from 'vue-router'
import showPdf from '@/components/showPdf'
import tagTree from '@/components/tagTree'
import login from '@/components/login'
import register from '@/components/register'
import index from '@/components/index'
Vue.use(Router)

export default new Router({
  routes: [
    /*
    {
      path: '/',
      name: 'showPdf',
      component: showPdf
    },
    */
    {
      path: '/',
      name: 'index',
      component: index,
      // children: [
    },
        {
          path: '/login',
          name: 'login',
          component: login,
        },
        {
          path: '/register',
          name: 'register',
          component: register,
        },
        {
          path: '/showPdf',
          name: 'showPdf',
          component: showPdf,
        },
        {
          path: '/tag',
          name: 'tagTree',
          component: tagTree
        },
      // ]
    // }
  ]
})
