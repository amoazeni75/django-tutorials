<template>
    <div id="app">
        <NavbarComponent/>
        <router-view/>
    </div>
</template>

<script>
    import NavbarComponent from "./components/Navbar"
    import {apiService} from "../common/api.service"

    export default {
        name: "App",
        components: {
            NavbarComponent
        },
        methods: {
            async getUserInfo() {
                const data = await apiService("/api/user/")
                const requestUser = data["username"]
                window.localStorage.setItem("username", requestUser)
            }
        },
        created() {
            this.getUserInfo()
        }
    }
</script>

<style>
    html, body {
        height: 100%;
        font-family: "Playfair Display", serif;
    }

    .btn:focus {
        box-shadow: none !important;
        /*this is because we do not have refresh in vue, so we need to disable focus*/
    }

</style>
