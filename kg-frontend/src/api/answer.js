import { request } from './index.js'
import qs from 'qs'

export function getAnswer(data) {
    return request({
        method: 'POST',
        url: 'answer/getAnswer',
        data: qs.stringify(data),
    })
}