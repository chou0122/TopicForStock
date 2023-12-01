import React from 'react'

export default function test() {
    <>

    點擊登入按鈕之後跳轉
    GET https://access.line.me/oautch2/v2.1/authorize
    登入成功後會轉到授權頁面，授權成功後會使用 redirect_uri 轉回我們的網站，並使用 Query String 帶上 authorization_code

    拿到 authorization_code 後，我們可以使用下面這個 API 獲得 access_token 
    POST https://api.line.me/oauth2/v2.1/token 
    拿到 access_token 後可以使用 Social API 取得用戶 UserId 登入我們的系統
    GET https://api.line.me/v2/profile
    </>
    
  return (
    <div>test</div>
  )
}
