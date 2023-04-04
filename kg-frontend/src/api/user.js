import { request } from './index.js'
import qs from 'qs'

//登录
export function login(data) {
    return request({
        method: 'POST',
        url: '/user/login',
        data: qs.stringify(data),
    })
}


//注册
export function register(data) {
    return request({
        method: 'POST',
        url: '/user/register',
        data: qs.stringify(data),
    })
}