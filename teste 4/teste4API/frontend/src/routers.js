import {createRouter, createWebHistory} from 'vue-router'
import MyHome from './components/MyHome'
import MySearchResult from './components/MySearchResult'

const routes = [
    {
        path:'/',
        name:'MyHome',
        component: MyHome
    },

    {
        path:'/MySearchResult/:searchType/:search',
        name:'MySearchResult',
        component:MySearchResult
    }
]

const router = createRouter({
    history:createWebHistory(),
    routes,
})

export default router;