const API = import.meta.env.VITE_API_URL || 'http://localhost:8000/api'
export function getToken(){return localStorage.getItem('devatlas_access')}
export async function api(path:string,options:RequestInit={}) {
 const token=getToken()
 const response=await fetch(`${API}${path}`,{...options,headers:{'Content-Type':'application/json',...(token?{Authorization:`Bearer ${token}`}:{}),...options.headers}})
 const data=await response.json().catch(()=>({}))
 if(!response.ok)throw new Error(data.detail||JSON.stringify(data)||'Request failed')
 return data
}
export async function login(email:string,password:string){
 const data=await api('/auth/token/',{method:'POST',body:JSON.stringify({username:email,password})})
 localStorage.setItem('devatlas_access',data.access);localStorage.setItem('devatlas_refresh',data.refresh)
}
export async function register(first_name:string,email:string,password:string){
 await api('/auth/register/',{method:'POST',body:JSON.stringify({first_name,email,password})});await login(email,password)
}
