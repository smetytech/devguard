<script lang="ts">
	import { pricingPacks } from 'src/data/pricing-packs.data';
	import { testimonials } from 'src/data/testimonials.data';

	$: isPricingIntervalMonthly = pricingInterval === 'MONTHLY';
	$: isPricingIntervalYearly = pricingInterval === 'YEARLY';

	let pricingInterval: 'MONTHLY' | 'YEARLY' = 'YEARLY';

	const groups = Array.from({ length: testimonials.length / 2 }, (_, i) => ({
		testimonials: testimonials.slice(i * 2, i * 2 + 2)
	}));
</script>

<svelte:head>
	<title>DevGuard</title>
</svelte:head>

<div class="relative">
	<img
		class="absolute left-1/2 top-4 z-[-1] -translate-x-1/2 opacity-75 blur lg:top-0"
		src="/images/svg/hero-background.svg"
		alt="hero background"
	/>

	<div class="mx-auto max-w-[80rem] space-y-32 px-4 py-8 lg:space-y-48 lg:px-6 lg:py-12">
		<section class="relative">
			<img
				class="absolute -top-4 right-0 z-[-1] hidden lg:block"
				src="/images/svg/graphic-1.svg"
				alt="graphic 1"
			/>

			<div class="space-y-6 lg:w-3/5">
				<h1
					class="text-center font-rubik text-6xl font-semibold leading-[4.25rem] lg:text-left lg:text-6xl lg:leading-[5rem]"
				>
					<span
						class="bg-gradient-to-r from-[#0084FF] via-[#FF8AC7] to-[#FEBA75] bg-clip-text text-transparent"
					>
						Actively Defending Your Infrastructure
					</span>
					<span>with DevGuard</span>
				</h1>

				<p class="text-center text-lg text-foreground/80 lg:pr-24 lg:text-left">
					Equipped with powerful tools like Trivy and Trufflehog, DevGuard scans your code for vulnerabilities, detects data leaks, and simulates potential attacks.
					Whether acting as a vigilant sentinel or a simulated adversary, DevGuard ensures your systems are ready to withstand emerging threats.
				</p>

				<div class="flex flex-col items-center gap-4 lg:flex-row">
					<a
						class="group w-fit rounded-2xl bg-gradient-to-l from-[#FFAB8F] via-[#FF8EC1] to-[#B67EFD] p-[0.0625rem]"
						href="/"
					>
						<div
							class="flex items-center gap-2.5 rounded-[calc(1rem-0.0625rem)] bg-gradient-to-t from-[#21223C] to-[#0B0B26] px-5 py-3.5 group-hover:to-[#21223C]"
						>
							<span
								class="bg-gradient-to-r from-[#B67EFD] via-[#F088D2] to-[#FFAD8B] bg-clip-text font-semibold leading-tight text-transparent"
							>
								Explore DevGuard
							</span>

							<svg
								class="stroke-[#FFAB8F]"
								width="20"
								height="20"
								viewBox="0 0 20 20"
								fill="none"
								xmlns="http://www.w3.org/2000/svg"
							>
								<path
									d="M7.50004 5C7.50004 5 12.5 8.68242 12.5 10C12.5 11.3177 7.5 15 7.5 15"
									stroke-width="1.25"
									stroke-linecap="round"
									stroke-linejoin="round"
								/>
							</svg>
						</div>
					</a>

					<a
						class="group rounded-2xl bg-gradient-to-tl from-[#4E4E69] to-[#4E4E69]/25 p-[0.0625rem]"
						href="/"
					>
						<div
							class="flex items-center gap-2.5 rounded-[calc(1rem-0.0625rem)] bg-gradient-to-t from-[#21223C] to-[#0B0B26] px-5 py-3.5 group-hover:to-[#21223C]"
						>
							<svg
								class="stroke-foreground"
								width="20"
								height="20"
								viewBox="0 0 20 20"
								fill="none"
								xmlns="http://www.w3.org/2000/svg"
							>
								<path
									d="M9.9974 18.3337C14.5998 18.3337 18.3307 14.6027 18.3307 10.0003C18.3307 5.39795 14.5998 1.66699 9.9974 1.66699C5.39502 1.66699 1.66406 5.39795 1.66406 10.0003C1.66406 14.6027 5.39502 18.3337 9.9974 18.3337Z"
									stroke-width="1.5"
								/>
								<path
									d="M12.875 10.3287C12.7487 10.8509 12.1521 11.22 10.959 11.9582C9.80548 12.6717 9.22881 13.0285 8.76398 12.8851C8.57181 12.8258 8.39681 12.7132 8.25558 12.558C7.91406 12.1828 7.91406 11.4551 7.91406 9.99967C7.91406 8.54426 7.91406 7.81649 8.25558 7.4413C8.39681 7.28618 8.57181 7.17357 8.76398 7.11428C9.22881 6.97087 9.80548 7.32765 10.959 8.0412C12.1521 8.77934 12.7487 9.14842 12.875 9.67067C12.9271 9.88626 12.9271 10.1131 12.875 10.3287Z"
									stroke="#CAD1E9"
									stroke-width="1.5"
									stroke-linejoin="round"
								/>
							</svg>

							<span class="font-semibold leading-tight">See How DevGuard Works</span>
						</div>
					</a>
				</div>
			</div>
		</section>

		<section class="grid items-center gap-8 lg:grid-cols-5 lg:gap-16" id="how-it-works">
			<div class="space-y-4 lg:col-span-3">
				<h2
					class="text-center font-rubik text-4xl font-medium leading-[2.75rem] lg:text-left lg:text-5xl lg:leading-[3.75rem]"
				>
					Strengthen Your Code with DevGuard’s Proactive Security
				</h2>

				<p class="text-center text-lg text-foreground/80 lg:text-left">
					DevGuard continuously scans your code with advanced tools like Trivy for vulnerability detection and Trufflehog for sensitive data leaks, fortifying your infrastructure against emerging threats.
				</p>
				<p class="text-center text-lg text-foreground/80 lg:text-left">
					Automate comprehensive security checks and address vulnerabilities proactively, before they impact your software.
				</p>
				<p class="text-center text-lg text-foreground/80 lg:text-left">
					With DevGuard, your code is not only protected, but rigorously tested through simulated attacks, ensuring resilient defenses at every stage.
				</p>
			</div>

			<img class="mx-auto lg:col-span-2" src="/images/svg/graphic-2.svg" alt="graphic 2" />
		</section>

		<section class="grid items-center gap-8 lg:grid-cols-2 lg:gap-16">
			<div class="space-y-4 lg:order-last">
				<h2
					class="text-center font-rubik text-4xl font-medium leading-[2.75rem] lg:text-left lg:text-5xl lg:leading-[3.75rem]"
				>
					DevGuard Shields Your Code from Exploits
				</h2>

				<p class="text-center text-lg text-foreground/80 lg:text-left">
					Ensure a robust development environment by securing your code against malicious attacks with DevGuard’s comprehensive vulnerability detection.
				</p>
			</div>

			<img class="mx-auto" src="/images/svg/graphic-3.svg" alt="graphic 3" />
		</section>

		<section class="space-y-16" id="features">
			<div class="space-y-4">
				<h2
					class="text-center font-rubik text-4xl font-medium leading-[2.75rem] lg:text-5xl lg:leading-[3.75rem]"
				>
					Why Choose DevGuard for Unmatched Security
				</h2>

				<p class="text-center text-lg text-foreground/80 lg:mx-48">
					DevGuard provides a complete security solution, integrating advanced vulnerability scanning, intelligent data leak detection, and proactive defenses to keep your code safe from all angles.
				</p>
			</div>

			<div class="grid gap-8 lg:grid-cols-2">
				<div class="rounded-2xl bg-gradient-to-br from-[#4E4E69] to-[#4E4E69]/25 p-[0.0625rem]">
					<div
						class="space-y-8 rounded-[calc(1rem-0.0625rem)] bg-gradient-to-t from-[#21223C] to-[#0B0B26] p-10"
					>
						<div class="space-y-4">
							<h3 class="font-rubik text-3xl font-medium leading-[2.25rem]">
								Vulnerability Detection and Removal
							</h3>

							<p class="text-lg text-foreground/80">
								We eliminate security vulnerabilities from your CI/CD pipelines using advanced automated scanning and manual intervention when necessary.
							</p>
						</div>

						<img src="/images/svg/graphic-4.svg" alt="graphic 4" />
					</div>
				</div>

				<div class="rounded-2xl bg-gradient-to-br from-[#4E4E69] to-[#4E4E69]/25 p-[0.0625rem]">
					<div
						class="space-y-8 rounded-[calc(1rem-0.0625rem)] bg-gradient-to-t from-[#21223C] to-[#0B0B26] p-10"
					>
						<div class="space-y-4">
							<h3 class="font-rubik text-3xl font-medium leading-[2.25rem]">
								Code Shielding and Threat Monitoring
							</h3>

							<p class="text-lg text-foreground/80">
								DevGuard proactively monitors and shields your code from potential exploits, offering real-time alerts and insights on security threats.
							</p>
						</div>

						<img src="/images/svg/graphic-5.svg" alt="graphic 5" />
					</div>
				</div>

				<div
					class="rounded-2xl bg-gradient-to-br from-[#4E4E69] to-[#4E4E69]/25 p-[0.0625rem] lg:col-span-2"
				>
					<div
						class="space-y-16 rounded-[calc(1rem-0.0625rem)] bg-gradient-to-t from-[#21223C] to-[#0B0B26] p-10"
					>
						<div class="grid gap-16 lg:grid-cols-2 lg:gap-24">
							<div class="space-y-8">
								<div class="space-y-4">
									<h3 class="font-rubik text-3xl font-medium leading-[2.25rem]">
										Interact with DevGuard Directly from Your Command Line
									</h3>

									<p class="text-lg text-foreground/80">
										Communicate directly with DevGuard through our intuitive Command Line Interface.
										Detect vulnerabilities, fix misconfigurations, and receive guidance on enhancing your code’s security—all within a seamless CLI experience.
										Whether you need a quick vulnerability scan or detailed advice on code security, DevGuard’s CLI agent is ready to assist.
									</p>
								</div>

								<div class="space-y-4">
									<img src="/images/svg/github-1.svg" alt="github 1" />

									<p class="text-lg text-foreground/80">
										DevGuard identifies and documents misconfigurations directly within the
										Dockerfile pull request.
									</p>
								</div>
							</div>

							<div class="flex flex-col gap-8">
								<img class="w-fit" src="/images/svg/graphic-6.svg" alt="graphic 6" />

								<div class="mt-auto space-y-4">
									<img src="/images/svg/github-2.svg" alt="github 2" />

									<p class="text-lg text-foreground/80">
										The fixes are then committed, ensuring a secure and streamlined development
										process.
									</p>
								</div>
							</div>
						</div>

						<a
							class="group mx-auto block w-fit rounded-2xl bg-gradient-to-l from-[#FFAB8F] via-[#FF8EC1] to-[#B67EFD] p-[0.0625rem]"
							href="/"
						>
							<div
								class="flex items-center justify-center gap-2.5 rounded-[calc(1rem-0.0625rem)] bg-gradient-to-t from-[#21223C] to-[#0B0B26] px-5 py-3.5 group-hover:to-[#21223C]"
							>
								<span
									class="bg-gradient-to-r from-[#B67EFD] via-[#F088D2] to-[#FFAD8B] bg-clip-text text-center font-semibold leading-tight text-transparent"
								>
									Explore DevGuard for free
								</span>

								<svg
									class="shrink-0 stroke-[#FFAB8F]"
									width="20"
									height="20"
									viewBox="0 0 20 20"
									fill="none"
									xmlns="http://www.w3.org/2000/svg"
								>
									<path
										d="M7.50004 5C7.50004 5 12.5 8.68242 12.5 10C12.5 11.3177 7.5 15 7.5 15"
										stroke-width="1.25"
										stroke-linecap="round"
										stroke-linejoin="round"
									/>
								</svg>
							</div>
						</a>
					</div>
				</div>
			</div>
		</section>

		<section class="space-y-16">
			<div class="space-y-4">
				<h2
					class="text-center font-rubik text-4xl font-medium leading-[2.75rem] lg:text-5xl lg:leading-[3.75rem]"
				>
					Why Developers Trust DevGuard to Secure Their Pipelines
				</h2>

				<p class="text-center text-lg text-foreground/80 lg:mx-48">
					DevGuard’s advanced security features provide peace of mind to developers by ensuring code safety and integrity.
					Here’s how our users have experienced DevGuard's impact on their workflows.
				</p>
			</div>

			<div class="grid gap-5 lg:grid-cols-4">
				{#each groups as group}
					<div class="space-y-5">
						{#each group.testimonials as testimonial}
							<div
								class="rounded-2xl bg-gradient-to-br from-[#4E4E69] to-[#4E4E69]/25 p-[0.0625rem]"
							>
								<div
									class="space-y-2 rounded-[calc(1rem-0.0625rem)] bg-gradient-to-t from-[#21223C] to-[#0B0B26] px-3 py-5"
								>
									<div class="flex items-center gap-3">
										<img
											class="h-9 w-9 rounded-full"
											src={testimonial.picture}
											alt={testimonial.name}
										/>

										<div>
											<span class="block text-xl font-medium leading-tight">{testimonial.name}</span
											>
											<span class="block">{testimonial.role}</span>
										</div>
									</div>

									<p class="text-foreground/80">
										{testimonial.message}
									</p>
								</div>
							</div>
						{/each}
					</div>
				{/each}
			</div>
		</section>

		<section class="space-y-16" id="pricing">
			<div class="space-y-4">
				<h2
					class="text-center font-rubik text-4xl font-medium leading-[2.75rem] lg:text-5xl lg:leading-[3.75rem]"
				>
					Find the Perfect DevGuard Plan for Your CI/CD Security
				</h2>

				<p class="text-center text-lg text-foreground/80 lg:mx-48">
					Choose a plan that fits your team’s security requirements, from essential protection to advanced monitoring and support.
					Every plan includes the tools needed to secure your CI/CD pipelines.
				</p>
			</div>

			<div class="space-y-16">
				<div
					class="mx-auto flex w-fit gap-2 rounded-2xl border border-[#2C2D47] bg-gradient-to-t from-[#70717A]/15 to-[#1B1C36]/15 p-1"
				>
					<button
						class={`${isPricingIntervalYearly ? 'bg-gradient-to-tl from-[#4E4E69] to-[#4E4E69]/25' : ''} group rounded-xl p-[0.0625rem]`}
						on:click={() => (pricingInterval = 'YEARLY')}
					>
						<div
							class={`${
								isPricingIntervalYearly
									? 'from-[#21223C] to-[#0B0B26]'
									: 'from-transparent to-transparent'
							} flex items-center gap-2.5 rounded-[calc(0.75rem-0.0625rem)] bg-gradient-to-t px-5 py-3.5 group-hover:to-[#21223C]`}
						>
							<span class="font-medium leading-tight">Billed yearly -20%</span>
						</div>
					</button>

					<button
						class={`${isPricingIntervalMonthly ? 'bg-gradient-to-tl from-[#4E4E69] to-[#4E4E69]/25' : ''} group rounded-xl p-[0.0625rem]`}
						on:click={() => (pricingInterval = 'MONTHLY')}
					>
						<div
							class={`${
								isPricingIntervalMonthly
									? 'from-[#21223C] to-[#0B0B26]'
									: 'from-transparent to-transparent'
							} flex items-center gap-2.5 rounded-[calc(0.75rem-0.0625rem)] bg-gradient-to-t px-5 py-3.5 group-hover:to-[#21223C]`}
						>
							<span class="font-medium leading-tight">Billed monthly</span>
						</div>
					</button>
				</div>

				<div class="grid items-center gap-6 lg:grid-cols-3">
					{#each pricingPacks as pack, index}
						<div
							class={`${index === 1 ? 'from-[#B67EFD] via-[#F088D2] to-[#FFAD8B] p-[0.125rem]' : 'from-[#4E4E69] to-[#4E4E69]/25 p-[0.0625rem]'} h-fit rounded-[2rem] bg-gradient-to-br`}
						>
							<div
								class={`${index === 1 ? 'rounded-[calc(2rem-0.125rem)] py-20' : 'rounded-[calc(2rem-0.0625rem)] py-12'} bg-gradient-to-t from-[#21223C] to-[#0B0B26] px-5`}
							>
								<div class="px-4">
									<h3 class="text-center text-2xl font-medium leading-none tracking-wide">
										{pack.name}
									</h3>

									<p class="mt-5 text-center text-foreground/80">{pack.description}</p>

									<div class="mt-5 space-y-2">
										<span
											class={`${index === 1 ? 'mx-auto w-fit bg-gradient-to-r from-[#B67EFD] via-[#F088D2] to-[#FFAD8B] bg-clip-text text-transparent' : 'text-foreground'} block text-center font-rubik text-6xl font-medium`}
										>
											{`$${isPricingIntervalMonthly ? pack.monthlyPrice : pack.yearlyPrice}`}
										</span>

										<span class="block text-center font-medium">Per month</span>
									</div>

									<div class="mx-auto mt-8 w-fit space-y-5">
										{#each pack.features as feature}
											<div class="flex items-center gap-3">
												<svg
													width="21"
													height="20"
													viewBox="0 0 21 20"
													fill="none"
													xmlns="http://www.w3.org/2000/svg"
												>
													<path
														opacity="0.4"
														d="M1.53906 10.0003C1.53906 14.9479 5.54985 18.9587 10.4974 18.9587C15.445 18.9587 19.4557 14.9479 19.4557 10.0003C19.4557 5.05278 15.445 1.04199 10.4974 1.04199C5.54985 1.04199 1.53906 5.05278 1.53906 10.0003Z"
														fill="#18F9A8"
													/>
													<path
														d="M14.5672 6.68365C14.788 7.08744 14.6397 7.59381 14.2359 7.81463C13.0931 8.43958 12.0199 9.74792 11.2004 11.0027C10.801 11.6143 10.4805 12.1839 10.2601 12.6003C10.1501 12.8081 10.0656 12.9767 10.0092 13.0921L9.92727 13.2632C9.79852 13.5447 9.52435 13.7318 9.21535 13.7489C8.90627 13.7659 8.61316 13.6102 8.45425 13.3446C8.19532 12.9117 7.78388 12.5165 7.40258 12.2151C7.2173 12.0686 7.05054 11.9531 6.93153 11.8752L6.75629 11.7656C6.35671 11.5374 6.21758 11.0287 6.44554 10.629C6.67354 10.2292 7.18248 10.0899 7.58226 10.3179L7.84479 10.481C7.99662 10.5804 8.20485 10.7248 8.43625 10.9077C8.61309 11.0475 8.8108 11.2156 9.01044 11.4092C9.22444 11.0247 9.49194 10.5708 9.80502 10.0913C10.6523 8.79408 11.9124 7.18572 13.4363 6.35235C13.84 6.13152 14.3464 6.27985 14.5672 6.68365Z"
														fill="#18F9A8"
													/>
												</svg>

												<span class="font-medium">{feature}</span>
											</div>
										{/each}
									</div>
								</div>

								<a
									class={`${index === 1 ? 'bg-gradient-to-l from-[#FFAB8F] via-[#FF8EC1] to-[#B67EFD]' : 'bg-gradient-to-tl from-[#4E4E69] to-[#4E4E69]/25'} group mt-8 block rounded-xl p-[0.0625rem]`}
									href="/"
								>
									<div
										class="rounded-[calc(0.75rem-0.0625rem)] bg-gradient-to-t from-[#21223C] to-[#0B0B26] px-5 py-3.5 group-hover:to-[#21223C]"
									>
										<span
											class={`${index === 1 ? 'bg-gradient-to-r from-[#B67EFD] via-[#F088D2] to-[#FFAD8B] bg-clip-text text-transparent' : 'text-foreground'} block text-center font-medium leading-tight`}
										>
											Request access
										</span>
									</div>
								</a>

								<span class="mt-3 block text-center font-medium text-foreground/80">
									{pack.savings}
								</span>
							</div>
						</div>
					{/each}
				</div>
			</div>
		</section>
	</div>
</div>
