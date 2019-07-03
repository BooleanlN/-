import {httpInstance} from '@/Api/httpInstance'

export default {
  getUserList: function (params) {
    return httpInstance.post('/manage/userList', params)
  },
  login: function (params) {
    return httpInstance.post('/auth/login', params)
  },
  userDelete: function (params) {
    return httpInstance.post('manage/userDelete', params)
  },
  userEdit: function (params) {
    return httpInstance.post('/manage/userEdit', params)
  },
  userAdd: function (params) {
    return httpInstance.post('/auth/registe', params)
  },
  userLoginOut: function (params) {
    return httpInstance.post('/auth/logout', params)
  },
  userRegiste: function (params) {
    return httpInstance.post('/auth/registe', params)
  }
}
