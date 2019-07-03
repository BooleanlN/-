import Vue from 'vue'
import Router from 'vue-router'
import routes from '@/router/router'
Vue.use(Router)

const router = new Router({
  routes: routes
})
router.beforeEach((to, from, next) => {
  if (window.sessionStorage.getItem('islogined') !== '1' && (to.fullPath !== '/login' && to.fullPath !== '/registe')) {
    next('/login')
  } else {
    next()
  }
})
export default router
