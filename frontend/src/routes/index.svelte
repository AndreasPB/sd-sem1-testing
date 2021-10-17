<script>
	import Footer from '../components/footer.svelte';
	import Navbar from '../components/navbar.svelte';
</script>

<body class="flex flex-col min-h-screen">
	<Navbar />
	<main class="flex-grow">
		<div class="container mx-auto">
			<h1>Welcome to SvelteKit</h1>
			<p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>
		</div>
	</main>
	<Footer />
</body>
