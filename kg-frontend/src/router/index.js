import Vue from 'vue'
import VueRouter from 'vue-router'

const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location, onResolve, onReject) {
    if (onResolve || onReject) {
        return originalPush.call(this, location, onResolve, onReject)
    }
    return originalPush.call(this, location).catch(err => err)
}

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        redirect: '/login'
    },
    {
        path: '/main',
        redirect: '/main/upload',
    },
    {
        path: '/main',
        component: () => import('views/main/Main.vue'),
        children: [
            {
                path: 'upload',
                component: () => import('views/main/upload/UploadFile.vue'),
            },
            {
                path: 'graph',
                component: () => import('views/main/graph/Graph.vue'),
            },
            {
                path: 'answer',
                component: () => import('views/main/answer/Answer.vue'),
            },
            {
                path: 'management',
                component: () => import('views/main/management/Management.vue'),
            },
        ]
    },
    {
        path: '/login',
        component: () => import('components/Login.vue')
    }
]

const router = new VueRouter({
    routes,
    mode: 'history'
})

// 导航守卫
router.beforeEach((to, from, next) => {
    if (to.path == ('/login') ){
        next()
    } else {
        if ( !localStorage.getItem('USER')) {
            next({ path: '/login' })
        } else {
            next()
        }
    }
})

export default router