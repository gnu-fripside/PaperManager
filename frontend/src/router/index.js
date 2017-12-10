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
                name: 'index',
                component: index,
                children: [
                    {
                        path: 'showPdf',
                        component: showPdf
                    },
                    {
                        path: 'tagTree',
                        component: tagTree
                    },
                    {
                        path: 'fileInfo',
                        component: fileInfo
                    }
                ]
            },
            {
                path: '/login',
                name: 'login',
                component: login
            },
            {
                path: '/register',
                name: 'register',
                component: register
            },
            {
                path: '/showPdfss',
                name: 'showPdf',
                component: showPdf
            },
            {
                path: '/tagss',
                name: 'tagTree',
                component: tagTree
            }
        ]
    }
)
