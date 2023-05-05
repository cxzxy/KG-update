import { request } from './index.js'
import qs from 'qs'

export function getSettings() {
    return request({
        method: 'GET',
        url: 'settings/getSettings',
    })
}

export function updateSettings(data) {
    return request({
        method: 'POST',
        url: 'settings/updateSettings',
        data: qs.stringify(data),
    })
}