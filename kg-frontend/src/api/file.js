import { request } from './index.js'
import qs from 'qs'

export function uploadFile(data) {
    return request({
        method: 'POST',
        url: '/file/uploadFile',
        data: qs.stringify(data),
    })
}

export function getSuccessFiles(data) {
    return request({
        method: 'POST',
        url: '/file/getSuccessFiles',
        data: qs.stringify(data),
    })
}
export function getUnauditedFiles(data) {
    return request({
        method: 'POST',
        url: '/file/getUnauditedFiles',
        data: qs.stringify(data),
    })
}
export function getFileDetail(data) {
    return request({
        method: 'GET',
        url: '/file/getFileDetail',
        params: data
    })
}

export function searchFile(data) {
    return request({
        method: 'POST',
        url: '/file/searchFileList',
        data: qs.stringify(data),
    })
}

export function examineFile(data){
    return request({
        method: 'POST',
        url: '/file/examineFile',
        data: qs.stringify(data)
    })
}