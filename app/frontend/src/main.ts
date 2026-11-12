import { createApp, h } from 'vue'
createApp({render:()=>h('main',[h('h1','校园助手开发环境'),h('p','基础环境已启动，业务功能尚未实现。'),h('a',{href:'/api/v1/health'},'检查后端连接')])}).mount('#app')
