// api request
import axios from 'axios';

export const get_campaigns = (access_token, email) => {
    return new Promise((resolve, reject) => {
        let url = `http://localhost:8000/campaigns`;
        axios.get(url)
            .then((res) => {
                if (!res.data.campaigns && res.data.campaigns.length === 0) return resolve(null);
                return resolve(res.data)
            })
            .catch(error => {
                console.log(error);
                return reject(error.response);
            });
    })
}