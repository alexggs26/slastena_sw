import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store/index.js'
import LayoutApp from '../components/LayoutApp.vue'
import AuthContainer from '../components/auth/AuthContainer.vue'
import RegisterContainer from '../components/register/RegisterContainer.vue'
import MainContainer from '../components/main/MainContainer.vue'


Vue.use(VueRouter)

const router = new VueRouter({
  mode: "history",
  routes: [
    {
      path: "/login",
      component: AuthContainer
    },
    {
      path: "/register",
      component: RegisterContainer
    },
    {
      path: "/app",
      component: LayoutApp,
      meta: { requiresAuth: true },
      children: [
        { path: 'main', component: MainContainer, meta: { requiresAuth: true } },
        // { path: 'sales/:monthyear', component: SalesContainer }
      ]
    },
    //     {path: "/business-process", component: BussinesProcess, meta: {requiresAuth: true}},
    //     {path: "/sales", component: SalesReport, meta: {requiresAuth: true}},
    //     {path: "/service", component: ServiceReport, meta: {requiresAuth: true}},
    //     {path: "/integration", component: IntegrationReport, meta: {requiresAuth: true}},
    //     {path: "/warehouse", component: WarehouseReport, meta: {requiresAuth: true}},
    //     {path: "/marketing", component: MarketingReport, meta: {requiresAuth: true}},
    //     {path: "/finance", component: FinanceReport, meta: {requiresAuth: true}},
    { path: '*', redirect: '/app/main' }
  ]
})


router.beforeEach((to, from, next) => {
  if (to.path === '/') next('/app/main')
  if (to.matched.some(route => route.meta.requiresAuth)) {
    if (store.getters.isLogged) {
      next();
    }
    else { next('/login') }
  } else {
    if (store.getters.isLogged) {
      if (to.path === '/login' || to.path === '/registration') next('/app/main')
      next();
    }
    next()
  }
})

export default router;
