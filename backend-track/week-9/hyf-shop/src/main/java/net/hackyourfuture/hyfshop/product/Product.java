package net.hackyourfuture.hyfshop.product;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

import java.math.BigDecimal;

@AllArgsConstructor
@NoArgsConstructor
@Builder
@Getter
public class Product {
    private int id;
    private String title;
    private BigDecimal price;
    private String category;
}
