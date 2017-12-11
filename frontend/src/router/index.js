import Vue from 'vue';
import Router from 'vue-router';
import showPdf from '@/components/showPdf';
import tagTree from '@/components/tagTree';
import login from '@/components/login';
import register from '@/components/register';
import index from '@/components/index';
import fileInfo from '@/components/fileInfo';
Vue.use(Router);

export default new Router(
    {
        routes: [
            {
                path: '/',
                alias: '/login',
                name: 'login',
                component: login
            },
            {
                path: '/user/:name',
                name: 'index',
                component: index,
                children: [
                    {
                        path: 'showPdf/:code',
                        name: 'showPdf',
                        component: showPdf
                    },
                    {
                        path: 'tagTree',
                        name: 'tagTree',
                        component: tagTree
                    },
                    {
                        path: 'fileInfo',
                        name: 'fileInfo',
                        component: fileInfo
                    }
                ]
            },
            {
                path: '/register',
                name: 'register',
                component: register
            }
        ]
    }
)
