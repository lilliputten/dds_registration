/* eslint-disable @typescript-eslint/no-explicit-any */

import { StripeConstructor } from '@stripe/stripe-js/dist/stripe-js';
// node_modules/@stripe/stripe-js/dist/stripe-js/index.d.ts

declare global {
  interface Window {
    STRIPE_PUBLISHABLE_KEY: string;
    billing_event_payment_stripe_create_checkout_session: Function;
    // Stripe.js must be loaded directly from https://js.stripe.com/v3, which
    // places a `Stripe` object on the window
    Stripe: StripeConstructor;
  }
}