# Website Deployment
The Website is hosted on [GitHub.io](https://jyablonski.github.io/) as well as on a [Personal Website](https://www.jyablonski.dev).

GitHub io can be used to build websites based off of flat files.

My Personal Website uses S3 to store the flat files, Cloudfront to host the user-facing site, and Route53 to take the Google-generated domain and re-route traffic to the Cloudfront instance.  The Google Domain costs $12 a year, the rest of the AWS Services fall under free-tier eligible.

# Tech Specifics

## S3
Based on what I did, S3 is a completely open bucket for read access.  Only I can write / delete to it, but 100% of the files in there are public.  
    * Cloudfront acts like the S3 bucket is essentially a normal "website" with public-facing traffic, and not really an S3 bucket.
    * This allows me to use the S3 feature to automatically use the `index.html` file in each sub-directory to serve the content without having to reroute traffic on a sub-directory using a JS or Lambda function.
    * S3 (the "origin" in this case) can only be read using `http` aka port 80, but all Cloudfront traffic is served with `https`.

## Route53
`www.jyablonski.dev` gets re-routed to the Cloudfront endpoint that gets created via Terraform (`xxxxx.cloudfront.net`).

The 2 SSL Certificates for `www.jyablonski.dev` and `jyablonski.dev` have their own `CNAME` Route53 record to make sure that credential can do what it needs to do to enable HTTPS.

## Certificates
You can request AWS to create SSL Certificates on your behalf to be able to utilize `https`.  To verify your identity, you can either verify through email, or be given CNAME key / value pairs that have to get added to either 1) Route53, or 2) Google Domain Options depending on your deployment.  This basically confirms that you own the Domain.

## Google Domain
2 Ways you can host a Google Domain on Cloudfront

1) Don't use Route53, and instead do all of the DNS stuff on the Google Domain side.  This involves uses Google Name Servers and sending all of the credential info and CNAME stuff in Google's Domain Options.

2) Use Route53 and select `Use Custom Name Servers` and attach AWS Name Server's to the Google Domain Options so the website uses them instead.

The `.dev` ending requires `https` traffic.