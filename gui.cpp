//INSTALL QT FOR GUI!!!!!!
#include <QApplication>
#include <QPushButton>
#include <QLineEdit>
#include <QLabel>
#include <QVBoxLayout>

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);

    QWidget window;
    window.setWindowTitle("Link Generator");

    QLabel *label1 = new QLabel("Forwarded link to localhost:80:");
    QLineEdit *link1Edit = new QLineEdit;

    QLabel *label2 = new QLabel("Forwarded link to localhost:3000:");
    QLineEdit *link2Edit = new QLineEdit;

    QPushButton *generateButton = new QPushButton("Generate");

    QVBoxLayout *layout = new QVBoxLayout;
    layout->addWidget(label1);
    layout->addWidget(link1Edit);
    layout->addWidget(label2);
    layout->addWidget(link2Edit);
    layout->addWidget(generateButton);

    window.setLayout(layout);
    window.show();

    return app.exec();
}
