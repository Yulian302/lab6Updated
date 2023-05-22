import { Triangle } from "./triangle";
import { IsoscelesTriangle } from "./isosceles_triangle";

describe('Triangle testing', () => {
    let iso_triangle: Triangle;
    beforeEach(() => {
        iso_triangle = new IsoscelesTriangle(100, 100, 100);
    });
    fit(("Creating class instance"), () => {
        expect(iso_triangle).toBeTruthy();
    });
});
