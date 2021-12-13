export default function loginCacheClear(loginWithRedirect){
  window.sessionStorage.clear()
  loginWithRedirect()
}