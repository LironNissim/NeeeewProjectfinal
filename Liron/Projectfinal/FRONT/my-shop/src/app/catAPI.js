import axios from 'axios'
const URL="http://127.0.0.1:8000/categories/"

export function getcats(){
    return new Promise((resolve)=>
        axios(URL).then((res)=> resolve({data: res.data}))
    );
}

    