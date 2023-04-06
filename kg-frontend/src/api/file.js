import { request } from './index.js'
import qs from 'qs'

export function uploadFile(data) {
    return request({
        method: 'POST',
        url: '/file/uploadFile',
        data: qs.stringify(data),
    })
}

export function getSuccessFiles() {
    return request({
        method: 'GET',
        url: '/file/getSuccessFiles',
    })
}