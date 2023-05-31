import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store/index.js'
import LayoutApp from '../components/LayoutApp.vue'
import AuthContainer from '../components/auth/AuthContainer.vue'
import RegisterContainer from '../components/register/RegisterContainer.vue'
import MainContainer from '../components/main/MainContainer.vue'
import ProvidersListContainer from '../components/providers/ProvidersListContainer.vue'
import ProviderContainer from '../components/providers/ProviderContainer.vue'


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
        { path: 'orders', component: MainContainer, meta: { requiresAuth: true } },
        { path: 'providers', component: ProvidersListContainer, meta: { requiresAuth: true } },
        { path: 'providers/details/:id', component: ProviderContainer, meta: { requiresAuth: true } },
        // { path: 'nomenclature', component: NomenclatureContainer, meta: { requiresAuth: true } },
      ]
    },
  ]
})


router.beforeEach((to, from, next) => {
  if (to.path === '/') next('/app/orders')
  if (to.matched.some(route => route.meta.requiresAuth)) {
    if (store.getters.isLogged) {
      next();
    }
    else { next('/login') }
  } else {
    if (store.getters.isLogged) {
      if (to.path === '/login' || to.path === '/registration') next('/app/orders')
      next();
    }
    next()
  }
})

export default router;
