import axios from 'axios'

export function request(config) {
    const instance = axios.create({
        baseURL: 'http://127.0.0.1:8081',
        timeout: 5000,
    })

    // 后端验证token，有token(未登录)去验证，没token直接越过
    //请求拦截器
    instance.interceptors.request.use(config => {
        const userinfo = localStorage.getItem('USER')
        if (userinfo) config.headers.Authorization = JSON.parse(userinfo).token
        return config
    })

    // //响应拦截器
    instance.interceptors.response.use(res => {
        return res.data
    }, err => {
        console.log(err)
    })

    return instance(config)
}
