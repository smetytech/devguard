import type { IPricingPack } from 'src/interfaces/pricing-pack.interface';

export const pricingPacks: Array<IPricingPack> = [
	{
		name: 'Starter',
		description:
			'Perfect for small teams or individual developers looking to start securing their CI/CD pipelines.',
		monthlyPrice: 0,
		yearlyPrice: 0,
		features: [
			'Vulnerability Scanning',
			'Basic Threat Detection',
			'Access to Core Modules',
			'Basic Security Alerts'
		],
		savings: 'It’s free so why not'
	},
	{
		name: 'Professional',
		description:
			'Ideal for growing teams who need more advanced features and in-depth security reports.',
		monthlyPrice: 25,
		yearlyPrice: 20,
		features: [
			'Everything in Starter',
			'Advanced Threat Detection',
			'Automated Fixes',
			'Priority Support'
		],
		savings: 'Save $60 per year'
	},
	{
		name: 'Enterprise',
		description:
			'Comprehensive security solution for large teams and enterprises with complex CI/CD needs.',
		monthlyPrice: 125,
		yearlyPrice: 100,
		features: [
			'Everything in Professional',
			'Custom Security Policies',
			'Dedicated Security Analyst',
			'Continuous Monitoring and Alerts'
		],
		savings: 'Save $300 per year'
	}
];
