import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import EditDream from '../views/EditDream'

const routes = [    
    {
        path:'/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/updatedream/:id',
        name: 'UpdateDream',
        component: EditDream,
        props: true
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router