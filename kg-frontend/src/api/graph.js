import { request } from './index.js'
import qs from 'qs'

//获取图谱数据
export function getGraphData(data) {
    return request({
        method: 'GET',
        url: 'graph/getGraph',
        params: data,
    })
}