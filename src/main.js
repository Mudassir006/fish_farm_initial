import { createApp } from 'vue';
import { createRouter, createWebHistory } from 'vue-router';
import App from './App.vue';
import AllComponentsView from './views/AllComponentsView.vue';
import CartView from './views/CartView.vue';
import AddressView from "@/views/AddressView";
import SummaryView from "@/views/SummaryView";
import   Keycloak from "keycloak-js";


const routes = [
  { path: '/', component: AllComponentsView },
  { path: '/cart/', component: CartView },
  { path: '/cart/address', component: AddressView },
  { path: '/cart/address/summary', component: SummaryView }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

const app = createApp(App);
app.use(router);
app.mount('#app');

const keycloakConfig = {
  url: 'http://localhost:8080/',
  realm: 'fishfarmpk',
  clientId: 'test-1',
    onLoad:'login_required',
    public:true

};

const keycloak =  new Keycloak(keycloakConfig);

keycloak
.init({ onLoad: 'check-sso', promiseType: 'native'})
.then((authenticated) => {
  if (authenticated) {
    console.log('User is authenticated');
    localStorage.setItem('accessToken', keycloak.token);
    localStorage.setItem('vueRefreshToken', keycloak.refreshToken);
    localStorage.setItem('idToken', keycloak.idToken)

    // startApp();
  } else {
    console.log('User is not authenticated');
  }
})
.catch((error) => {
  console.error('Keycloak initialization error:', error);
});

      keycloak.onAuthSuccess = () => {
      setInterval(() => {
        keycloak
            .updateToken(60)
            .then((refreshed) => {
            if (refreshed) {
                console.debug('Token refreshed', refreshed);
                console.log(keycloak.token)
                localStorage.setItem('accessToken', keycloak.token);
                localStorage.setItem('vueRefreshToken', keycloak.refreshToken);

              } else {
                console.warn(
                'Token not refreshed, valid for ' +
                    Math.round(
                    (keycloak.tokenParsed.exp +
                        keycloak.timeSkew -
                        new Date().getTime()) /
                        1000
                    ) +
                    ' seconds'
                );
            }
            })
            .catch((error) => {
            console.log(error);
            });
        }, 60000);
      };

      export default keycloak