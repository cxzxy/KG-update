import { request } from './index.js'
import qs from 'qs'

export function getPermission(data) {
    return request({
        method: 'POST',
        url: '/permission/getPermissionList',
        data: qs.stringify(data)
    })
}

export function updatePermission(data){
    return request({
        method: 'POST',
        url: '/permission/changePermission',
        data: JSON.stringify(data)
    })
}

export function guardAdmin(data){
    return request({
        method: 'POST',
        url: '/permission/guardAdmin',
        data: qs.stringify(data)
    })
}