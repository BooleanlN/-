import Main from '@/components/Main'
import Login from '@/components/Login'
import UserTable from '@/pages/user-table'
import LowPowerUser from '@/pages/low-power-user-table'
import Knowlege from '@/pages/knowledge-in'
import KnowlegeTable from '@/pages/knowledge-table'
import KnowlegeExcelIn from '@/pages/knowledge-excel-in'
import LowPowerUserAdd from '@/pages/low-power-user-add'
import Registe from '@/components/Registe'
const childRoutes = [
  {
    name: 'userTable',
    path: '/main/usertable',
    component: UserTable
  }, {
    name: 'lowPowerUserAdd',
    path: '/main/lowpowerusersadd',
    component: LowPowerUserAdd
  }, {
    name: 'lowPowerUser',
    path: '/main/lowpowerusers',
    component: LowPowerUser
  }, {
    name: 'knowledgeImport',
    path: '/main/knowledge',
    component: Knowlege
  }, {
    name: 'knowledgeTable',
    path: '/main/knowledgeTable',
    component: KnowlegeTable
  }, {
    name: 'knowledgeExcelImport',
    path: '/main/knowlegeexcel',
    component: KnowlegeExcelIn
  }
]
const routes = [
  {
    path: '/',
    redirect: '/main/usertable'
  },
  {
    path: '/main',
    name: 'main',
    component: Main,
    redirect: '/main/usertable',
    children: childRoutes
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    name: 'registe',
    path: '/registe',
    component: Registe
  }
]
export default routes
