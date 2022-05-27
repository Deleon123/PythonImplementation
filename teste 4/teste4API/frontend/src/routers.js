import {createRouter, createWebHistory} from 'vue-router'
import MyHome from './components/MyHome'
import MySearch from './components/MySearch'

const routes = [
    {
        path:'/',
        name:'MyHome',
        component: MyHome
    },

    {
        path:'/MySearch',
        name:'MySearch',
        component:MySearch
    }
]

const router = createRouter({
    history:createWebHistory(),
    routes,
})

export default router;