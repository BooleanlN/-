import axios from 'axios'
let httpInstance = axios.create({
  baseURL: '',
  timeout: 1000,
  headers: {'Content-type': 'application/x-www-form-urlencoded'}
})
let httpFileInstance = axios.create({
  baseURL: '',
  timeout: 1000,
  headers: {'Content-type': 'multipart/form-data'}
})
// 请求前拦截器，将数据转为json格式
httpInstance.interceptors.request.use(config => {
  return config
}, error => {
  return Promise.reject(error)
})
// 请求后拦截器，判断请求是否成功
httpInstance.interceptors.response.use(
  response => {
    if (response.status === 200 && response.data.code === 1) {
      return Promise.resolve(response.data)
    } else {
      return Promise.reject(response.data)
    }
  },
  error => {
    return Promise.reject(error)
  }
)
httpFileInstance.interceptors.response.use(
  response => {
    if (response.status === 200 && response.data.code === 1) {
      return Promise.resolve(response.data)
    } else {
      return Promise.reject(response.data)
    }
  },
  error => {
    return Promise.reject(error)
  }
)
export {httpInstance, httpFileInstance}
