<template>
    <div id="app">
        <NavbarComponent/>
        <router-view/>
    </div>
</template>

<script>
    import NavbarComponent from "./components/Navbar"

    export default {
        name: "App",
        components: {
            NavbarComponent
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
