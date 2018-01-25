## Intro


    ```
    python3 setup.py build_ext --inplace
    ```


    ```
    pip install -e .
    ```

    ```
    pip install .
    ```

## run
python flow --model cfg/yolo.cfg --load bin/yolo.weights --demo videofile.mp4 --gpu 1.0 --saveVideo
