import Vue from 'vue'
import Router from 'vue-router'
import showPdf from '@/components/showPdf'
import tagTree from '@/components/tagTree'

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
      name: 'tagTree',
      component: tagTree
    }
  ]
})
