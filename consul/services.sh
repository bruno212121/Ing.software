#!/bin/bash
docker exec -i consul consul services register -name=ArticlesOrderApi -address=article.order.com
docker exec -i consul consul services register -name=ShippingOrderApi -address=shipping.order.com