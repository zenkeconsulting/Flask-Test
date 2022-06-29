<template>
	<div class="layout-footer">
        <div class="footer-logo-container">
            <img id="footer-logo" :src="'layout/images/logo-'+ (colorScheme === 'light' ? 'dark' : 'light') + '.png'" alt="atlantis-layout"/>
            <span class="app-name">ATLANTIS</span>
        </div>
        <span class="copyright">&#169; Your Organization - 2022</span>
    </div>
</template>

<script>
export default {
	props: {
		colorScheme: String
	}
}
</script>

