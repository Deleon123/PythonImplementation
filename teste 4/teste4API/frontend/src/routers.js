import {createRouter, createWebHistory} from 'vue-router'
import MyHome from './components/MyHome'
import MyCreate from './components/MyCreate'

const routes = [
    {
        path:'/',
        name:'MyHome',
        component:MyHome
    },
    
    {
        path:'/MyCreate',
        name:'MyCreate',
        component:MyCreate
    }
]

const router = createRouter({
    history:createWebHistory(),
    routes,
})

export default router;